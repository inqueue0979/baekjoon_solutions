#include <iostream>

int main()
{

    std::string chess_bw[8] = {"BWBWBWBW","WBWBWBWB","BWBWBWBW","WBWBWBWB","BWBWBWBW","WBWBWBWB","BWBWBWBW","WBWBWBWB"};
    std::string chess_wb[8] = {"WBWBWBWB","BWBWBWBW","WBWBWBWB","BWBWBWBW","WBWBWBWB","BWBWBWBW","WBWBWBWB","BWBWBWBW"};

    int size_x, size_y, ans_bw = 0, ans_wb = 0, lowest = 250000;
    std::cin >> size_y >> size_x;

    std::string* datas = new std::string[size_y];

    for(int i = 0; i < size_y; i++)
        std::cin >> datas[i];
    

    for(int i = 0; i < size_y - 7; i++)
        for(int j = 0; j < size_x - 7; j++)
        {
            ans_bw = 0, ans_wb = 0;
            for(int k = i; k < i + 8; k++)
                for(int l = j; l < j + 8; l++)
                {
                    if(datas[k][l] != chess_bw[k-i][l-j])
                        ans_bw++;
                    else if(datas[k][l] != chess_wb[k-i][l-j])
                        ans_wb++;
                }

            if(ans_bw < lowest) lowest = ans_bw;
            if(ans_wb < lowest) lowest = ans_wb;
            
        }

    std::cout << lowest;

    return 0;
}