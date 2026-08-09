// Heuristic discovery search for a 31-point deletion from ER(17).
//
// This program is NOT part of the proof of the theorem: its output is checked
// exhaustively by the Python verifiers. It is included to reproduce the
// discovery route. With libstdc++ and the archived command (seed 2603), it
// finds the archived seed-2603 certificate at iteration 786389 in the recorded environment.
//
// Build:
//   g++ -O3 -std=c++17 search_polarity_deletion.cpp -o search_polarity_deletion
// Run:
//   ./search_polarity_deletion 17 31 16 2603 5000000 replay.json 1

#include <bits/stdc++.h>
using namespace std;

struct Search {
  int q, n, deletion_count, target_min_degree;
  vector<array<int, 3>> points;
  vector<vector<int>> adjacency;
  vector<int> ambient_degree, deletion_capacity;
  mt19937_64 rng;

  Search(int q_, int deletion_count_, int target_, uint64_t seed)
      : q(q_),
        n(q_ * q_ + q_ + 1),
        deletion_count(deletion_count_),
        target_min_degree(target_),
        rng(seed) {
    for (int a = 0; a < q; ++a)
      for (int b = 0; b < q; ++b) points.push_back({1, a, b});
    for (int b = 0; b < q; ++b) points.push_back({0, 1, b});
    points.push_back({0, 0, 1});

    adjacency.assign(n, {});
    for (int i = 0; i < n; ++i) {
      for (int j = i + 1; j < n; ++j) {
        long dot = 0;
        for (int k = 0; k < 3; ++k) dot += (long)points[i][k] * points[j][k];
        if (dot % q == 0) {
          adjacency[i].push_back(j);
          adjacency[j].push_back(i);
        }
      }
    }

    ambient_degree.resize(n);
    deletion_capacity.resize(n);
    for (int i = 0; i < n; ++i) {
      ambient_degree[i] = (int)adjacency[i].size();
      deletion_capacity[i] = ambient_degree[i] - target_min_degree;
    }
  }

  inline int vertex_penalty(int v, const vector<uint8_t>& deleted,
                            const vector<uint8_t>& deleted_neighbors) const {
    if (deleted[v]) return 0;
    int excess = (int)deleted_neighbors[v] - deletion_capacity[v];
    return excess > 0 ? 1000 + 100 * excess * excess + excess : 0;
  }

  int score(const vector<uint8_t>& deleted,
            const vector<uint8_t>& deleted_neighbors) const {
    int result = 0;
    for (int v = 0; v < n; ++v)
      result += vertex_penalty(v, deleted, deleted_neighbors);
    return result;
  }

  int bad_vertices(const vector<uint8_t>& deleted,
                   const vector<uint8_t>& deleted_neighbors) const {
    int result = 0;
    for (int v = 0; v < n; ++v)
      result += (!deleted[v] && deleted_neighbors[v] > deletion_capacity[v]);
    return result;
  }

  void recompute_counts(const vector<uint8_t>& deleted,
                        vector<uint8_t>& deleted_neighbors) {
    fill(deleted_neighbors.begin(), deleted_neighbors.end(), 0);
    for (int x = 0; x < n; ++x)
      if (deleted[x])
        for (int v : adjacency[x]) ++deleted_neighbors[v];
  }

  void initialize(vector<uint8_t>& deleted,
                  vector<uint8_t>& deleted_neighbors) {
    fill(deleted.begin(), deleted.end(), 0);
    vector<int> vertices(n);
    iota(vertices.begin(), vertices.end(), 0);
    shuffle(vertices.begin(), vertices.end(), rng);
    for (int i = 0; i < deletion_count; ++i) deleted[vertices[i]] = 1;
    recompute_counts(deleted, deleted_neighbors);
  }

  int swap_delta(int remove_from_deleted, int add_to_deleted,
                 vector<uint8_t>& deleted,
                 vector<uint8_t>& deleted_neighbors) {
    vector<int> affected;
    affected.reserve(2 * q + 4);
    vector<uint8_t> seen(n);
    auto add_affected = [&](int v) {
      if (!seen[v]) {
        seen[v] = 1;
        affected.push_back(v);
      }
    };
    add_affected(remove_from_deleted);
    add_affected(add_to_deleted);
    for (int v : adjacency[remove_from_deleted]) add_affected(v);
    for (int v : adjacency[add_to_deleted]) add_affected(v);

    int old_penalty = 0;
    for (int v : affected)
      old_penalty += vertex_penalty(v, deleted, deleted_neighbors);

    deleted[remove_from_deleted] = 0;
    deleted[add_to_deleted] = 1;
    for (int v : adjacency[remove_from_deleted]) --deleted_neighbors[v];
    for (int v : adjacency[add_to_deleted]) ++deleted_neighbors[v];

    int new_penalty = 0;
    for (int v : affected)
      new_penalty += vertex_penalty(v, deleted, deleted_neighbors);

    deleted[remove_from_deleted] = 1;
    deleted[add_to_deleted] = 0;
    for (int v : adjacency[add_to_deleted]) --deleted_neighbors[v];
    for (int v : adjacency[remove_from_deleted]) ++deleted_neighbors[v];
    return new_penalty - old_penalty;
  }

  void apply_swap(int remove_from_deleted, int add_to_deleted,
                  vector<uint8_t>& deleted,
                  vector<uint8_t>& deleted_neighbors) {
    deleted[remove_from_deleted] = 0;
    deleted[add_to_deleted] = 1;
    for (int v : adjacency[remove_from_deleted]) --deleted_neighbors[v];
    for (int v : adjacency[add_to_deleted]) ++deleted_neighbors[v];
  }

  void save(const string& filename, const vector<uint8_t>& deleted) const {
    ofstream output(filename);
    output << "[";
    bool comma = false;
    for (int i = 0; i < n; ++i) {
      if (deleted[i]) {
        if (comma) output << ",";
        comma = true;
        output << i;
      }
    }
    output << "]\n";
  }

  bool run(long long steps, int restarts, const string& output_file) {
    vector<uint8_t> deleted(n), deleted_neighbors(n);
    uniform_real_distribution<double> uniform(0.0, 1.0);
    int global_best = INT_MAX;

    for (int restart = 0; restart < restarts; ++restart) {
      initialize(deleted, deleted_neighbors);
      int current_score = score(deleted, deleted_neighbors);
      double temperature = 2200.0;
      int stagnant = 0;

      for (long long iteration = 0; iteration < steps; ++iteration) {
        int bad = bad_vertices(deleted, deleted_neighbors);
        if (current_score < global_best) {
          global_best = current_score;
          save(output_file + ".best", deleted);
          cerr << "best=" << current_score << " bad=" << bad
               << " r=" << restart << " i=" << iteration << "\n";
          if (!bad) {
            save(output_file, deleted);
            cout << "FOUND\n";
            return true;
          }
        }

        int remove_from_deleted, add_to_deleted;
        if (bad && uniform(rng) < 0.88) {
          vector<int> bad_list;
          for (int v = 0; v < n; ++v)
            if (!deleted[v] && deleted_neighbors[v] > deletion_capacity[v])
              bad_list.push_back(v);
          int v = bad_list[rng() % bad_list.size()];
          if (uniform(rng) < 0.55) {
            add_to_deleted = v;
            do
              remove_from_deleted = rng() % n;
            while (!deleted[remove_from_deleted]);
          } else {
            vector<int> deleted_neighbors_of_v;
            for (int x : adjacency[v])
              if (deleted[x]) deleted_neighbors_of_v.push_back(x);
            remove_from_deleted =
                deleted_neighbors_of_v[rng() % deleted_neighbors_of_v.size()];
            do
              add_to_deleted = rng() % n;
            while (deleted[add_to_deleted]);
          }
        } else {
          do
            remove_from_deleted = rng() % n;
          while (!deleted[remove_from_deleted]);
          do
            add_to_deleted = rng() % n;
          while (deleted[add_to_deleted]);
        }

        int delta = swap_delta(remove_from_deleted, add_to_deleted, deleted,
                               deleted_neighbors);
        double effective_temperature = max(0.1, temperature);
        if (delta <= 0 ||
            uniform(rng) < exp(-delta / effective_temperature)) {
          apply_swap(remove_from_deleted, add_to_deleted, deleted,
                     deleted_neighbors);
          current_score += delta;
          stagnant = delta < 0 ? 0 : stagnant + 1;
        } else {
          ++stagnant;
        }

        temperature *= 0.99997;
        if (temperature < 0.1) temperature = 0.1;
        if (stagnant > 300000) {
          initialize(deleted, deleted_neighbors);
          current_score = score(deleted, deleted_neighbors);
          temperature = 2200.0;
          stagnant = 0;
        }
      }
    }
    return false;
  }
};

int main(int argc, char** argv) {
  if (argc < 7) {
    cerr << "usage: q deletion_count target_min_degree seed steps output [restarts]\n";
    return 2;
  }
  int q = atoi(argv[1]);
  int deletion_count = atoi(argv[2]);
  int target = atoi(argv[3]);
  uint64_t seed = strtoull(argv[4], nullptr, 10);
  long long steps = atoll(argv[5]);
  string output = argv[6];
  int restarts = argc > 7 ? atoi(argv[7]) : 100;

  Search search(q, deletion_count, target, seed);
  return search.run(steps, restarts, output) ? 0 : 1;
}
