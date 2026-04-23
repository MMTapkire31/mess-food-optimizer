#include <bits/stdc++.h>
using namespace std;

struct Item {
    string name;
    int price, value;
};

int main() {
    ifstream in("input.txt");
    ofstream out("output.txt");

    int budget, n;
    in >> budget >> n;

    vector<Item> items(n);

    for(int i = 0; i < n; i++) {
        in >> items[i].name >> items[i].price >> items[i].value;
    }

    sort(items.begin(), items.end(), [](Item a, Item b) {
        return (double)a.value/a.price > (double)b.value/b.price;
    });

    int total = 0, total_value = 0;

    for(auto item : items) {
        if(total + item.price <= budget) {
            out << item.name << " (Rs." << item.price << ", Value " << item.value << ")" << endl;
            total += item.price;
            total_value += item.value;
        }
    }

    out << "TOTAL " << total << endl;
    out << "VALUE " << total_value << endl;

    return 0;
}