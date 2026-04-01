class Solution 
{

    public String encode(List<String> strs) 
    {
        if (strs.size() == 1 && strs.get(0) == "")
            return "";
        else if (strs.isEmpty())
            return null;

        String enc = "";

        for (String word : strs)
        {
            enc += word + "-";
        }

        return enc;
    }

    public List<String> decode(String str) 
    {
        if (str == null)
            return new ArrayList<>();
        else
            return Arrays.asList(str.split("-"));
    }
}
