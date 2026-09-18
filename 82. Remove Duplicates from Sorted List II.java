class Solution {
    public ListNode deleteDuplicates(ListNode head) {
        ListNode d = new ListNode(0);
        d.next = head;

        ListNode p = d;

        while (head != null) {
            if (head.next != null && head.val == head.next.val) {
                int x = head.val;

                while (head != null && head.val == x) {
                    head = head.next;
                }

                p.next = head;
            } else {
                p = p.next;
                head = head.next;
            }
        }

        return d.next;
    }
}