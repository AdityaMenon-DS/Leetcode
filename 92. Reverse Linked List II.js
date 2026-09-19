var reverseBetween = function(head, left, right) {
    if (left === right) {
        return head;
    }

    let d = new ListNode(0);
    d.next = head;

    let p = d;

    for (let i = 1; i < left; i++) {
        p = p.next;
    }

    let a = p.next;
    let b = a.next;

    for (let i = 0; i < right - left; i++) {
        a.next = b.next;
        b.next = p.next;
        p.next = b;
        b = a.next;
    }

    return d.next;
};