class Solution {
    public Node copyRandomList(Node head) {
        if (head == null) {
            return null;
        }

        Node cur = head;

        while (cur != null) {
            Node copy = new Node(cur.val);
            copy.next = cur.next;
            cur.next = copy;
            cur = copy.next;
        }

        cur = head;

        while (cur != null) {
            if (cur.random != null) {
                cur.next.random = cur.random.next;
            }
            cur = cur.next.next;
        }

        cur = head;
        Node ans = head.next;

        while (cur != null) {
            Node copy = cur.next;

            cur.next = copy.next;

            if (copy.next != null) {
                copy.next = copy.next.next;
            }

            cur = cur.next;
        }

        return ans;
    }
}