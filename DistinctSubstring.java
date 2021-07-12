import java.util.HashSet;
import java.util.Iterator;
import java.util.Set;
import java.util.*;  
  
public class DistinctSubstring {
  
    public static int distinctSubstring(String str)
    {
        // Put all distinct substring in a HashSet
        Set<String> result = new HashSet<String>();
  
        // List All Substrings
        for (int i = 0; i <= str.length(); i++) {
            for (int j = i + 1; j <= str.length(); j++) {
  
                // Add each substring in Set
                result.add(str.substring(i, j));
            }
        }
  
        // Return size of the HashSet
        return result.size();
    }
  
    // Driver Code
    public static void main(String[] args)
    {   
        Scanner sc= new Scanner(System.in); 
        String str = sc.nextLine(); 
        System.out.println(distinctSubstring(str));
    }
}