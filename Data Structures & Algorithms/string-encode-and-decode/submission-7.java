class Solution 
{

    public String encode(List<String> strs) 
    {
        if (strs.size() == 1 && strs.get(0) == "")
            return "";
        else if (strs.isEmpty())
            return null;
        
        String encodedString = "";

        for (String word : strs)
        {
            encodedString += word + "-";
        }

        return encodedString;
    }

    public List<String> decode(String str) 
    {
        if (str == null)
            return new ArrayList<String>();
        else
            return Arrays.asList(str.split("-"));
    }
}
