public class twoSum{
    public int[] twoSum(int[] nums, int target) {

        for(int i=0; i<nums.length; i++){
            for(int j=i+1; j<nums.length; j++){ //j+1 bc you dont want to compare an index with itself... no length-1 bc you want to compare all elements
                if(nums[i] + nums[j] == target){
                    return new int[] {i , j};
                } 
            }
        } throw new IllegalArgumentException("There is no possible solution"); // here bc if after the first wring combination, it would throw an error... want it to check all possible solutions.