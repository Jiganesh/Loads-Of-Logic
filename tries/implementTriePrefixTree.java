//https://leetcode.com/problems/implement-trie-prefix-tree/

/* Time complexity: O(n) : insert and search
Auxiliary space: O(n)*/

package tries;

import java.io.*;
import java.util.*;

class Trie {
  
  //Trie structure
  class TrieNode{
     TrieNode [] children;
     boolean isEnd;
    public TrieNode() {
        children = new TrieNode[26];
        isEnd = false;
    }
   }
  
    private final TrieNode root;
  
    public Trie() {
        root = new TrieNode();
    }
    
  //insert function in Trie
    public void insert(String word) {
        TrieNode curr = root;
        for(int indx = 0; indx<word.length(); indx++){
            char c = word.charAt(indx);
             int ind = c - 'a';
            if(curr.children[ind] == null){
                curr.children[ind] = new TrieNode();
            }
            curr = curr.children[ind];
        }
        curr.isEnd = true;
    }
    
    //search function in Trie
    public boolean searchWord(String word) {
        TrieNode curr = root;
        for(int indx = 0; indx<word.length(); indx++){
            char c = word.charAt(indx);
             int ind = c - 'a';
            if(curr.children[ind] == null){
               return false;
            }
            curr = curr.children[ind];
        }
        return curr.isEnd == true;
    }
    
    //checking prefix function in Trie
    public boolean checkstartsWith(String prefix) {
        TrieNode curr = root;
        for(int indx = 0; indx<prefix.length(); indx++){
            char c = prefix.charAt(indx);
            int ind = c - 'a';
            if(curr.children[ind] == null){
                return false;
            }
            curr = curr.children[ind];
        }
        return true;
    }
}
