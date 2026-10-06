class Solution {
    public ListNode sortList(ListNode head) {
        if (head == null || head.next == null) {
            return head;
        }

        int n = 0;
        ListNode p = head;

        while (p != null) {
            n++;
            p = p.next;
        }

        ListNode dummy = new ListNode(0);
        dummy.next = head;

        for (int size = 1; size < n; size *= 2) {
            ListNode cur = dummy.next;
            ListNode tail = dummy;

            while (cur != null) {
                ListNode left = cur;
                ListNode right = split(left, size);
                cur = split(right, size);

                tail = merge(left, right, tail);
            }
        }

        return dummy.next;
    }

    private ListNode split(ListNode head, int size) {
        if (head == null) {
            return null;
        }

        for (int i = 1; i < size && head.next != null; i++) {
            head = head.next;
        }

        ListNode next = head.next;
        head.next = null;

        return next;
    }

    private ListNode merge(ListNode a, ListNode b, ListNode tail) {
        while (a != null && b != null) {
            if (a.val <= b.val) {
                tail.next = a;
                a = a.next;
            } else {
                tail.next = b;
                b = b.next;
            }

            tail = tail.next;
        }

        tail.next = (a != null) ? a : b;

        while (tail.next != null) {
            tail = tail.next;
        }

        return tail;
    }
}