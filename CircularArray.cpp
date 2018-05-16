//REQUIRED TASK 2

#include <iostream.h>
#include<conio.h>
//#include<vector.h>
//#include<algorithm.h>


template <class data_type> class circularArray
{
	int n;
	data_type arr[30];
	public:
	void input();

	void circular();

};

template <class data_type> void circularArray<data_type>::input()
{
	 cout<<"Enter the no of elements in the circular array[canot be greater than 30]:";
	 cin>>n;

	 cout<<"Enter the elements of the array:";
	 for(int i=0;i<n;i++)
	 { cin>>arr[i];
	  }
	 }

template <class data_type> void circularArray<data_type>::circular()
{

		data_type ele;
		int flag=0;
		cout<<"Enter the element of a circular array:";
		cin>>ele;
		int index;

		//checking for the element in the array
	    //for (data_type element : arr) -----compiler not supporting this
	       for(int i=0;i<n;i++)
		{
		  if(ele==arr[i])
		 {
		    index=i;
		    flag=1;
		    break;
		 }
		}


		//Circular Array Application
		if(flag==0)
		{
		 cout<<"The element is not present in the array"<<endl;
		}
		else
		{
		   int k=index;
		  // for(data_type element:arr)
		  for(i=0;i<n;i++)
		   {
			if(k==n-1)
			{
				cout<<arr[k]<<endl;
				k=0;
			}
			else
			{
				cout<<arr[k]<<endl;
				k=k+1;
			}
		   }
		}
 }

void main()
{
	circularArray<int> cr1;
	cr1.input();
	cr1.circular();

	circularArray<char> cr2;
	cr2.input();
	cr2.circular();

	getch();

}