#include<stdio.h>
#include<stdlib.h>
#include<time.h>
#include<unistd.h>
#define CONX 40    //life_ground's row
#define CONY 150   //life_ground's arrow

void pri_Group(int gr[CONX][CONY]);
void delay(unsigned long usec);

int main(void)
 {
   int life_ground[CONX][CONY];
   int life_ground_cur[CONX][CONY];
   int step = 500;
   char jud_chr;
   float ratio = 100; 
   float rand_pop;
   float posb;    
   int rand_comp;
   int pop_around = 0;
   int gib = 3; 
   int slu = 2;
   int reg_row = 4, reg_arr = 40, p_row = 20, p_arr = 60;

   int rand_x, rand_y, posx, posy;
   int low_birth = 3;
   int up_birth = 3;
   int evl_speed = 240;
   int die_jud; 

   system("clear");
   printf("\n\n=====================================================================\n");
   printf("----------------------------Life Game--------------------------------\n");
   printf("=====================================================================\n");

   printf("Do you want to change the default parameters?(Y/N):");
   scanf(" %c", &jud_chr);
  
   if ('Y'==jud_chr || 'y'==jud_chr)
    {
     // system("sl");
   
      printf("\nPlease assign the postion of the birthplace.\n(separated by spaces)(1~%d 1~%d):", CONX-1, CONY-1);
      scanf("%d %d", &p_row, &p_arr);
   
      printf("\nPlease input the size of the birthplace.\n(separated by spaces)(1~%d 1~%d):", CONX-1-p_row, CONY-1-p_arr);
      scanf("%d %d", &reg_row, &reg_arr);
   
      printf("\nPlease assign the survival rate in birthplace at the begining(persentage)(1~100):");
      scanf("%f", &ratio);
      
      printf("\nPlease input the LOWER & UPPER limit of life around for one's continue exist\n(0~8 <= ex <= 0~8)(separated by spaces):");
      scanf("%d %d",&slu , &gib);
   
      printf("\nPlease input the LOWER & UPPER limit of life around for a birth\n(0~8 <= bi <= 0~8)(separated by spaces):");
      scanf("%d %d", &low_birth, &up_birth);
   
      printf("\nPlease input the steps you need to observe:");
      scanf("%d", &step);
  
      printf("\nPLease input the evolution speed(ms per step):");
      scanf("%d", &evl_speed);
    }


//############################################################
//*******************Random life******************************
//############################################################
   
   srand((unsigned)time(NULL));   //A seed of random number

   rand_pop = reg_row * reg_arr * ratio / 100.00;
   rand_pop /= 1;

   rand_comp = 0;
   //printf("-------------%f----------------", rand_pop);
   
   for (int i1=0; i1<CONX; i1++)
     {
       for (int i2=0; i2<CONY; i2++)
         {
           life_ground[i1][i2] = 0;
           life_ground_cur[i1][i2] = 0; 
         }
     }                               //initialize all group mumber to zero

    int rand_assig = 0;
    while (rand_assig<rand_pop)
     {
       rand_x = rand()%reg_row+p_row;
       rand_y = rand()%reg_arr+p_arr;
   
      // printf ("(%d %d)", rand_x, rand_y);
   
       if (life_ground[rand_x][rand_y]==0)
         {
           life_ground[rand_x][rand_y] = 1;
           rand_assig ++;   
         }
     }                             //random assignment 

    system("clear");
    pri_Group(life_ground);        //show the random result
    delay(4000000);

//############################################################
//*******************Life Begin*******************************
//############################################################

   for (int sumcir=0; sumcir<step; sumcir++)
     {           
       delay(evl_speed*1000);           //delay evl_speed ms
       system("clear");          //clean last life picture

       for (int posx=1; posx<CONX-1; posx++)
         { 
           for (int posy=1; posy<CONY-1; posy++)
             {
               pop_around = life_ground[posx-1][posy-1]+life_ground[posx][posy-1]
                           +life_ground[posx+1][posy-1]+life_ground[posx-1][posy]
                           +life_ground[posx+1][posy]+life_ground[posx-1][posy+1]
                           +life_ground[posx][posy+1]+life_ground[posx+1][posy+1];  
 
               if (pop_around<=gib && pop_around>=slu)
                 {  
                  if (life_ground[posx][posy]==0 && pop_around>=low_birth && pop_around<=up_birth) 
                    life_ground_cur[posx][posy] = 1;    //live or birth
                 }
               else
                 {
                    life_ground_cur[posx][posy] = 0;   //die
                 }
             }
         }                                         //recard the life info in a temperary form
         
         for (int i1=0; i1<CONX; i1++)
           {
             for (int i2=0; i2<CONY; i2++)
               {
                 life_ground[i1][i2] = life_ground_cur[i1][i2];
               }      
           }                                      //give the life info to main form

         pri_Group(life_ground); 
          
         die_jud = 0;
         for (int i1=0; i1<CONX; i1++)
           {
             for (int i2=0; i2<CONY; i2++)
               {
                 if (life_ground[i1][i2]!=0)
                  die_jud ++;
               }      
           }                                      //die?

         if (die_jud==0)
          {
            system("clear");            
            printf("=======================You are DIE!!!=======================\n");
                      
            break;
          }
      }

   return 0;
 }


//############################################################
//*******************Defined functions************************
//############################################################

void pri_Group(int gr[CONX][CONY])
  {
    for (int i=0; i<CONX; i++)
      {
        printf("\n");
        for (int j=0; j<CONY; j++)
          {
             if(gr[i][j]==0)
               {
                 printf(" ");
               }
             else if (gr[i][j]==1)
               {
                 printf("●");
               }
           // printf("%d", gr[i][j]);
          }
      }


  }

void delay(unsigned long usec)
{
    clock_t now, start;
 
    start = clock();
    do
    {
        now = clock();
    }
    while(now - start < usec);
}
