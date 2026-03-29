
#note: i added the attributes 'title' in message_details because in the homework they ask in the search_inbox function
# if a string is in the body or in the title of a message
#for efficiency i let this attribute as a must and not optinal


class PostOffice:
    """A Post Office class. Allows users to message each other.

    Args:
        usernames (list): Users for which we should create PO Boxes.

    Attributes:
        message_id (int): Incremental id of the last message sent.
        boxes (dict): Users' inboxes.
    """

    def __init__(self, usernames):
        self.message_id = 0
        self.boxes = {user: [] for user in usernames}

    def send_message(self, sender, recipient, message_body, title,urgent=False):   #recipient=dest
        """Send a message to a recipient.

        Args:
            sender (str): The message sender's username.
            recipient (str): The message recipient's username.
            message_body (str): The body of the message.
            urgent (bool, optional): The urgency of the message.
                                    Urgent messages appear first.

        Returns:
            int: The message ID, auto incremented number.

        Raises:
            KeyError: If the recipient does not exist.

        Examples:
            After creating a PO box and sending a letter,
            the recipient should have 1 message in the
            inbox.


        """
        user_box = self.boxes[recipient]     # self.boxes = {user: [] for user in usernames}  -here by reference because list is mutable objetc
        self.message_id = self.message_id + 1
        message_details = {
            'id': self.message_id,
            'body': message_body,
            'sender': sender,
            'title': title,
        }
        if urgent:
            user_box.insert(0, message_details)  #add to a strict index
        else:
            user_box.append(message_details)
        return self.message_id


    def read_inbox(self,reader,N=0):
        """Send a message to a recipient.

               Args:
                   reader (str): the user who wants to read his inbox.
                   N (int, optional): The number of messages to send.


               Returns:
                   list : the messages he read.

               Raises:
                   KeyError: If N is not an integer or too big .

               """

        response=""
        messages = self.boxes[reader]     #a list

        if N<0 or  N>messages.__len__():
            raise KeyError("invalid N")
        if N==0:
            N=self.boxes[reader].__len__()

        for i in range(N):
            response = response+" "+messages[0]['body']
            messages.remove(self.boxes[reader][0])    #remove the mesage from the queue

        return response


    def search_inbox(self,searcher,stringToSearch):
        """Search a string in the inbox.

                       Args:
                           searcher (str): the user who wants to search the string.
                           stringToSearch (str): The string to search for.


                       Returns:
                           list : the messages or title that contains the string.
                           """

        user_box = self.boxes[searcher]   #a list
        response=[]
        for msg in user_box:
            if stringToSearch in msg['body']:
                response = response + [msg['body']]
            if stringToSearch in msg['title']:
                response = response + [msg['title']]

        if response:

            return response
        else:

            return ""
"""
tests: ------------------

PO_box = PostOffice(['a', 'b','c'])
PO_box.send_message('a', 'b', 'HellofromA!','tell u Hello!')
PO_box.send_message('c', 'b', 'HelloFromC!','tezll from c')
PO_box.send_message('c', 'b', 'what doing today!','activity')
PO_box.search_inbox('b','Hello')
PO_box.read_inbox('b')

PO_box.read_inbox('b')
PO_box.send_message('a', 'b', 'why you dont answering!','reponse!')
PO_box.read_inbox('b')

"""

