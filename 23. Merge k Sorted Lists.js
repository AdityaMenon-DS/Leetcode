/*
23. Merge k Sorted Lists
Hard
Topics
premium lock icon
Companies
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

 

Example 1:

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted linked list:
1->1->2->3->4->4->5->6
Example 2:

Input: lists = []
Output: []
Example 3:

Input: lists = [[]]
Output: []
 

Constraints:

k == lists.length
0 <= k <= 104
0 <= lists[i].length <= 500
-104 <= lists[i][j] <= 104
lists[i] is sorted in ascending order.
The sum of lists[i].length will not exceed 104.
*/
var mergeKLists = function(lists) {
    if (lists.length === 0) {
        return null;
    }

    function merge(a, b) {
        let d = new ListNode(0);
        let p = d;

        while (a !== null && b !== null) {
            if (a.val <= b.val) {
                p.next = a;
                a = a.next;
            } else {
                p.next = b;
                b = b.next;
            }

            p = p.next;
        }

        if (a !== null) {
            p.next = a;
        } else {
            p.next = b;
        }

        return d.next;
    }

    while (lists.length > 1) {
        let a = [];

        for (let i = 0; i < lists.length; i += 2) {
            let x = lists[i];
            let y = i + 1 < lists.length ? lists[i + 1] : null;

            a.push(merge(x, y));
        }

        lists = a;
    }

    return lists[0];
};