class Solution {
    public ListNode rotateRight(ListNode head, int k) {
        if (head == null || head.next == null || k == 0) {
            return head;
        }

        int n = 1;
        ListNode a = head;

        while (a.next != null) {
            a = a.next;
            n++;
        }

        k = k % n;

        if (k == 0) {
            return head;
        }

        a.next = head;

        int steps = n - k;
        ListNode b = a;

        while (steps > 0) {
            b = b.next;
            steps--;
        }

        ListNode ans = b.next;
        b.next = null;

        return ans;
    }
}