/* package codechef; // don't place package name! */

import java.util.*;
import java.lang.*;
import java.io.*;

/* Name of the class has to be "Main" only if the class is public. */
class Codechef
{
	public static void main (String[] args) throws java.lang.Exception
	{
		// your code goes here
		Scanner in = new Scanner(System.in);
		int t= in.nextInt();
		while(t-- >0)
		{
		    int n=in.nextInt();
		    long k=in.nextLong();
		    int[] arr=new int[n];
		    int[] a = new int[3];
		    for(int i=0;i<n;i++)
		    {
		        arr[i]=in.nextInt();
		    }
		    long mul=k/n;
		    long rk=k%n;
		    for(int i=0;i<n;i++)
		    {
        	     int num=(int)mul;
                 if(i<rk)
                	num++;
        	     if(num==0)
        	     {
        	         System.out.print(arr[i]+" ");
        	     }
        	     else
        	     {
        	      if(n%2!=0 &&i==n/2 )
        	      {
        	          System.out.print(0+" ");
        	      }
        		      
        		  else
        	      {
        		      a[1]=arr[i]^arr[n-i-1];
        		      a[2]=arr[n-i-1];
        		      a[0]=arr[i];
        		      
        		      num=num%3;
        		      
        		      arr[i] =a[num];
        		      System.out.print(arr[i]+" ");
        		      arr[i]=a[0]^a[2];
        	      }
        	    
        	     }

        	}
        	System.out.println();
		
	}
		
	}
}
