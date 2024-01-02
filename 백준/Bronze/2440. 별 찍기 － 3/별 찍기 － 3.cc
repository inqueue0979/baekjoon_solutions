#include <iostream>

int main() {
    int a;
    std::cin >> a;
    
    for(int i = a-1; i >= 0; i--)
    {
        for(int j = 0; j <= i; j++)
            std::cout << "*";

        std::cout << "\n";
    }

    return 0;
}