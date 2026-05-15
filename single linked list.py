head = None

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

def sll(arr):
    global head

    head=tail=None
    for data in arr:
        new_node = Node(data)
        if head == None:
            head=tail=new_node
        else:
            tail.next=new_node
            tail=new_node

def traversal():
    temp=head
    if temp==None:
        print("Linked list is empty")
    while temp:
        print(temp.data,end = "->")
        temp=temp.next
    print("None")

def insert_at_beginning(data):
    global head

    new_node=Node(data)
    new_node.next=head
    head = new_node

def insert_at_end(data):
    global head

    new_node=Node(data)
    if head == None:
        head = new_node
        return
    temp = head
    while temp.next:
        temp=temp.next
    temp.next=new_node

def insert_after(prev_note,data):
    global head

    new_node = Node(data)
    temp = head
    if head == None:
        head=new_node
        return
    while temp:
        if temp.data == prev_note:
            new_node.next=temp.next
            temp.next = new_node
            return
        temp = temp.next
    print("Not found")

def deletion_at_beginning():
    global head

    if head==None:
        print("Linked list is empty")
        return
    head= head.next

def deletion_at_end():
    global head

    if head==None or head.next==None:
        print("linked list is empty")
        return
    temp=head
    while temp.next.next:
        temp=temp.next
    temp.next=None

def deletion_by_key(key):
    global head

    if head==None:
        print("Linked List is empty")
        return
    elif head.data==key:
        head=head.next
    temp=head
    while temp.next:
        if temp.next.data==key:
            temp.next=temp.next.next
        temp=temp.next

def deletion_by_position(index):
    global head

    if head==None:
        print("list is empty")
        return
    elif index==0:
        head=head.next
        return
    temp=head;count=0
    # move to node before target position
    while temp and count < index - 1:
        temp = temp.next
        count += 1

    # invalid index
    if temp is None or temp.next is None:
        print("Invalid index")
        return

    # delete node
    temp.next = temp.next.next

def detect_loop():
    global head
    slow=fast=head     

    while fast and fast.next:
        slow=slow.next
        fast=fast.next.next
        if slow ==fast:
            print("loop detected")
            return
    print("loop not found")  

def reverse_linked_list():
    global head

    prev_node=None;temp=head
    while temp:
        next_node=temp.next
        temp.next=prev_node
        prev_node=temp
        temp=next_node
    head=prev_node

def find_middle():
    global head

    slow=fast=head
    while fast and fast.next:
        slow =slow.next
        fast = fast.next.next
    print("Middle Node :",slow.data) 

def merge_sorted_lists(l1,l2):
    global head

    dummy=Node(0)
    tail=dummy
    while l1 and l2:
        if l1.data<l2.data:
            tail.next=l1
            l1=l1.next
        else:
            tail.next=l2
            l2=l2.next
        tail=tail.next
    tail.next = l1 or l2
    head = dummy.next
     

while True:
    print("\n===== Singly Linked List Operations =====")
    print("1. Create Linked List")
    print("2. Traversal")
    print("3. Insert at Beginning")
    print("4. Insert at End")
    print("5. Find Middle")
    print("6. Insert After")
    print("7. Delete at Beginning")
    print("8. Delete at End")
    print("9. Delete by Key")
    print("10. Delete by Position")
    print("11. Detect Loop")
    print("12. Reverse Linked List")
    print("13. Merge two sorted linked list")
    print("14.Exit")

    choice = int(input("Enter your choice: "))

    match choice:

        case 1:
            arr = list(map(int, input("Enter the linked list sequence with spaces:").split()))
            sll(arr)

        case 2:
            traversal()

        case 3:
            value = int(input("Enter value to insert at beginning: "))
            insert_at_beginning(value)
            print(f"Insert {value} at beginning of the linked list..")

        case 4:
            value = int(input("Enter value to insert at end: "))
            insert_at_end(value)
            print(f"Inserted {value} at end of the linked list..")

        case 5:
            find_middle()

        case 6:
            key = int(input("Insert after which value: "))
            value = int(input("Enter new value: "))
            insert_after(key, value)
            print(f"Inserted {value} after {key} in Linked List..")

        case 7:
            deletion_at_beginning()
            print("Deleted Node beginning of Linked List..")

        case 8:
            deletion_at_end()
            print("Deleted Node at end of the Linked List..")

        case 9:
            key = int(input("Enter key to delete: "))
            deletion_by_key(key)
            print(f"Deleted {key} Node from the Linked List..")

        case 10:
            pos = int(input("Enter position to delete: "))
            deletion_by_position(pos)
            print(f"Deleted Node at Position {pos} in the Linked List..")

        case 11:
            detect_loop()

        case 12:
            reverse_linked_list()
            print("Linked List Reversed")

        case 13:
            LL1 = list(map(int, input("Enter the 1st linked list sequence with spaces:").split()))
            LL2 = list(map(int, input("Enter the 2nd linked list sequence with spaces:").split()))
            sll(LL1)
            l1 = head
            traversal()
            sll(LL2)
            l2 = head
            traversal()
            print("Merged Sorted Linked List:")
            merge_sorted_lists(l1,l2)
            traversal()


        case 14:
            print("Exiting...")
            break

        case _:
            print("Invalid Choice!")

    print("\nCurrent Linked List:")
    traversal()