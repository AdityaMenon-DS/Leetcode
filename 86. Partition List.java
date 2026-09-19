class Solution {
    public ListNode partition(ListNode head, int x) {
        ListNode a = new ListNode(0);
        ListNode b = new ListNode(0);

        ListNode p = a;
        ListNode q = b;

        while (head != null) {
            if (head.val < x) {
                p.next = head;
                p = p.next;
            } else {
                q.next = head;
                q = q.next;
            }

            head = head.next;
        }

        q.next = null;
        p.next = b.next;

        return a.next;
    }
}