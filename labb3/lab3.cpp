
#include <iostream>
#include <cstdio>

int main()
{
    while (true) 
    {
        std::cout << "Choose the chunk size (1 for 1 GiB or 2 for 1 KiB): ";
        int choice;
        std::cin >> choice;
		int64_t GiB = 1073741824; 
		int64_t KiB = 1024; 
		int64_t size;
        switch (choice) 
        {
            case 1:
                size=GiB / sizeof(int64_t);
                break;
            case 2:
                size=KiB/ sizeof(int64_t);
                break;
            default:
                std::cout << "Invalid option. Try again." << std::endl;
                continue;
        }

        try
        {
            int* array = new int[size];
            std::cout << "Allocated memory: " << size * sizeof(int64_t) << " bytes" << std::endl;
            delete[] array;
        }
        catch (const std::bad_alloc& ba)
        {
            std::cout << "Allocation failed: " << ba.what() << std::endl;
        }
    }

    return 0;
}



