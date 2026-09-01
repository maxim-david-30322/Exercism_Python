#include "speedywagon.h"

namespace speedywagon {

// Enter your code below:

bool connection_check(pillar_men_sensor* ptr)
    {

        if(ptr==nullptr)
            return false;
                else
            return true;
    }

// int activity_count(pillar_men_sensor* sensor_array,int no)
//     {
//         int* number=&sensor_array[0]
//         int sum=0;
//         for (int i=0;i<no;i++)
//             {
//                 sum+=*number;
//                 number=(sensor_array+i);
//             }
//         return sum;
//     }
int activity_counter(pillar_men_sensor* sensor_array,int no)
    {
        int sum=0;
        for (int i=0;i<no;i++)
            {
                sum+=(sensor_array+i)->activity;
            }
        return sum;
    }

    
bool alarm_control(pillar_men_sensor* sensor_array){
    if(connection_check(sensor_array))
    {
        if(sensor_array->activity>0)
        return true;
        else
            return false;     
    }
    else
        return false;
    
}

bool uv_alarm(pillar_men_sensor* sensor)
    {
        if(connection_check(sensor))
        {
            if(uv_light_heuristic(&sensor->data)>sensor->activity)
                return true;
            else 
                return false;
        }
        else
                return false;
    }



    


    
// Please don't change the interface of the uv_light_heuristic function
int uv_light_heuristic(std::vector<int>* data_array) {
    double avg{};
    for (auto element : *data_array) {
        avg += element;
    }
    avg /= data_array->size();
    int uv_index{};
    for (auto element : *data_array) {
        if (element > avg) ++uv_index;
    }
    return uv_index;
}

}  // namespace speedywagon
