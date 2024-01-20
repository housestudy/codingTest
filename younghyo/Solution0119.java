/* 240119 프로그래머스 lv.2 호텔대실 */
// 정렬 , 탐색 
package codingTest;

import java.util.*;
import java.text.SimpleDateFormat;
import java.text.ParseException;

class Solution0119 {
	
	public int Solution(String[][] book_time)
	{
	
		SimpleDateFormat format = new SimpleDateFormat("HH:MM");
		
		Arrays.sort(book_time, Comparator.comparing((String[] s) -> s[0]).thenComparing(s ->s[1]));
		PriorityQueue<Date> queue = new PriorityQueue<>();
		
		try
		{
			Date date = new Date(format.parse(book_time[0][1]).getTime());
			Calendar calendar = Calendar.getInstance();
			calendar.setTime(date);
			calendar.add(Calendar.MINUTE, 10);
	
			queue.add(calendar.getTime());
			
			for(int i = 1; i<book_time.length; i++)
			{
				Date endTime = queue.peek();
				Date start = new Date(format.parse(book_time[i][0]).getTime());
				Date end = new Date(format.parse(book_time[i][1]).getTime());
				
				Calendar endCalc = Calendar.getInstance();
				endCalc.setTime(end);
				endCalc.add(Calendar.MINUTE, 10);
				
				if(endTime.compareTo(start) <= 0)
				{
					queue.poll();
				}			
			}
			
		}
		catch (ParseException e) 
		{
			e.printStackTrace();
		}	
		
		return queue.size();
	
	}
}
