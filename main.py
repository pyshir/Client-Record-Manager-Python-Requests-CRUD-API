import requests as req

class ReqMethods:

    def __init__(self):
        self.link = 'https://jsonplaceholder.typicode.com/posts/'
        self.headers = {
    'User-Agent' : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/154.0.0.0 Safari/537.36'

}

    def __add__(self, other):
        return self.link + other

    def get_method(self, ln):
        try:
            response = req.get(
                ln,
                timeout = 10,
                headers = self.headers
            )
            response.raise_for_status()
            data = response.json()
            print(
                f"\n\nRecord Found.......!\n"
                f"Id: {data['id']}\n"
                f"Title: {data['title']}\n"
                f"Body: {data['body']}\n"
                f"UserID: {data['userId']}\n"
            )

        except req.exceptions.RequestException as error:
            print(
                f'Record Not Found\n{error}'
            )

    def post_method(self, payloads):

        try:
            response = req.post(
                self.link,
                headers = self.headers,
                timeout = 10,
                json = payloads
            )
            response.raise_for_status()
            data = response.json()
            print(
                f'Post Created successfully..!\n'
                f'title: {data["title"]}\nbody: {data["body"]}\nId: {data["id"]}'
            )

        except req.exceptions.RequestException as error:
            print(f'Failed to create, try again\n{error}')

    def put_method(self,ln, payloads):

        try:
            response = req.put(
                ln,
                headers = self.headers,
                json = payloads,
                timeout = 10
                
            )
            response.raise_for_status()
            data = response.json()
            print(f"********Replaced*****\n\ntitle: {data['title']}\nbody: {data['body']}\nPost id: {data['id']}")

        except req.exceptions.RequestException as error:
            print(f'Failed to replace, Please try again\n{error}')

    def patch_method(self, ln, payloads):

        try:
            response = req.patch(
                ln,
                headers = self.headers,
                json = payloads,
                timeout = 10
            )
            response.raise_for_status()
            data = response.json()
            print('*********Update successful*********')
            for i, j in data.items():
                print(f'{i}: {j}')

        except req.exceptions.RequestException as error:
            print(f'Can\'t update, try again\n{error}')

    def delete_method(self, ln):
        try:
            response = req.delete(
                ln,
                headers = self.headers,
                timeout = 10
            )
            response.raise_for_status()
            print('********Successfully deleted********')

        except req.exceptions.RequestException as error:
            print(f'Can\'t delete, try again\n{error}')



if __name__ == '__main__':

    reqmethods = ReqMethods()

    while True:

        print("""
    ========== Client Record Manager ==========

    1. View Record
    2. Create Record
    3. Replace Record
    4. Update Record
    5. Delete Record
    6. Exit

    Choose an option: \n
    """)

        
        choice = input('= ')

        if choice == '1':
            try:
                post_id = int(input('Input post Id: '))
            except ValueError:
                print("Number Only")
                continue

            link = reqmethods + post_id            

            reqmethods.get_method(link)

        elif choice == '2':

            title = input('Enter title: \n=')
            body = input('Enter body: \n=')
            payloads = {
                'title' : title,
                'body' : body
            }
            reqmethods.post_method(payloads)

        elif choice == '3':
            title = input('Enter title: \n=')
            body = input('Enter body: \n=')
            try:
                post_id = int(input('Input post Id: '))
            except ValueError:
                print("Number Only")
                continue
            payloads = {
                'title' : title,
                'body' : body,
            }
            link = reqmethods.link + post_id
            reqmethods.put_method(link, payloads)

        elif choice == '4':

            try:
                post_id = int(input('Input post Id: '))
            except ValueError:
                print("Number Only")
                continue
            link = reqmethods + post_id
            print("""
1. Title
2. Body
""")
            choice_4 = input('Enter Choice: \n = ')
            payloads = {}
            if choice_4 == '1':
                title = input('Input Title: \n = ')
                payloads['title'] = title
                reqmethods.patch_method(link, payloads)
            elif choice_4 == '2':
                body = input('Input body text: \n= ')
                payloads['body'] = body
                reqmethods.patch_method(link, payloads)

            else:
                print('Enter number only (1 or 2)')

        elif choice == '5':

            try:
                post_id = int(input('Input post Id: '))
            except ValueError:
                print("Number Only")
                continue
            link = reqmethods + post_id

            reqmethods.delete_method(link)

        elif choice == '6':
            break

        else:
            print('Enter number only (1 to 6)')
            