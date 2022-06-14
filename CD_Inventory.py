
# Title: Assignment08.py
# Desc: Assignment 08 - Working with classes and functions

# -- DATA -- #
strFileName = 'cdInventory.txt'
lstOfCDObjects = []


class CD:
    """Stores data about a CD:

    properties:
        cd_id: (int) with CD ID
        cd_title: (string) with the title of the CD
        cd_artist: (string) with the artist of the CD
    methods:

    """
    # Add Code to the CD class
    def add_data(self, cd_id, cd_title, cd_artist):
        cd_id = int(cd_id)
        rows = {'ID': cd_id, 'Title': cd_title, 'Artist': cd_artist}
        lstOfCDObjects.append(rows)


# -- PROCESSING -- #
class FileIO:
    """Processes data to and from file:

    properties:

    methods:
        save_inventory(file_name, lst_Inventory): -> None
        load_inventory(file_name): -> (a list of CD objects)

    """
    # Add code to process data from a file
    def load_inventory(self, file_name, table):
        with open(file_name, 'r') as file:
            for line in file:
                data = line.strip().split(',')
                row = {'ID': int(data[0]), 'Title': data[1], 'Artist': data[2]}
                table.append(row)

    # Add code to process data to a file
    def save_inventory(self, file_name, table):
        with open(file_name, 'w') as file:
            for row in table:
                lstValues = list(row.values())
                lstValues[0] = str(lstValues[0])
                file.write(','.join(lstValues) + '\n')

# -- PRESENTATION (Input/Output) -- #
class IO:
    # add docstring
    """ Handles input and output
    Gets user input for menu selection

        Args:
            None.

        Returns:
            choice (string): a lower case sting of the users input out of the choices l, a, i, d, s or x

        """
    # add code to show menu to user
    def print_menu(self):
        """Displays a menu of choices to the user

        Args:
            None.

        Returns:
            None.
        """

        print('Menu\n\n[l] load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
        print('[s] Save Inventory to file\n[x] exit\n')

    # add code to captures user's choice
    def menu_choice(self):
        """Gets user input for menu selection

        Args:
            None.

        Returns:
            choice (string): a lower case sting of the users input out of the choices l, a, i, d, s or x

        """
        choice = ' '
        while choice not in ['l', 'a', 'i', 's', 'x']:
            choice = input('Which operation would you like to perform? [l, a, i, s or x]: ').lower().strip()
        print()  # Add extra space for layout
        return choice

    # add code to display the current data on screen
    def show_inventory(table):
        """Displays current inventory table


        Args:
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime.

        Returns:
            None.

        """
        print('======= The Current Inventory: =======')
        print('ID\tCD Title (by: Artist)\n')
        for row in table:
            print('{}\t{} (by:{})'.format(*row.values()))
        print('======================================')

    # add code to get CD data from user
    def ask_cd_info(self):
        cd_id = input('Enter ID: ').strip()
        cd_title = input('What is the CD\'s title? ').strip()
        cd_artist = input('What is the Artist\'s name? ').strip()
        result = (cd_id, cd_title, cd_artist)
        return result


# read_file = FileIO()
# read_file.load_inventory(strFileName, lstOfCDObjects)
# -- Main Body of Script -- #
def cd_inventory():
    while True:
        # Display Menu to user and get choice
        menu = IO()
        menu.print_menu()
        user_choice = menu.menu_choice()

        # process exit first
        if user_choice == 'x':
            break
        # process load inventory
        if user_choice == 'l':
            print('WARNING: If you continue, all unsaved data will be lost and the Inventory re-loaded from file.')
            strYesNo = input('type \'yes\' to continue and reload from file. otherwise reload will be canceled ')
            if strYesNo.lower() == 'yes':
                print('reloading...')
                load_file = FileIO()
                load_file.load_inventory(strFileName, lstOfCDObjects)
                IO.show_inventory(lstOfCDObjects)
            else:
                input('canceling... Inventory data NOT reloaded. Press [ENTER] to continue to the menu.')
                IO.show_inventory(lstOfCDObjects)
            continue
        # process add a CD
        elif user_choice == 'a':
            # Ask user for new ID, CD Title and Artist
            new_input = IO()
            result = new_input.ask_cd_info()
            # Add item to the table
            add_result = CD()
            add_result.add_data(result[0], result[1], result[2])
            IO.show_inventory(lstOfCDObjects)
            continue
        # process display current inventory
        elif user_choice == 'i':
            IO.show_inventory(lstOfCDObjects)
            continue
        # process save inventory to file
        elif user_choice == 's':
            # Display current inventory and ask user for confirmation to save
            IO.show_inventory(lstOfCDObjects)
            strYesNo = input('Save this inventory to file? [y/n] ').strip().lower()
            # Process choice
            if strYesNo == 'y':
                # save data
                save_file = FileIO()
                save_file.save_inventory(strFileName, lstOfCDObjects)
            else:
                input('The inventory was NOT saved to file. Press [ENTER] to return to the menu.')
            continue
        # catch-all should not be possible, as user choice gets vetted in IO, but to be save:
        else:
            print('General Error')


if __name__ == "__main__":
    cd_inventory()
