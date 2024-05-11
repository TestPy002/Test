#include <stdio.h>
#include <stdlib.h>
#include <string.h>
typedef struct 
{
    char name[50];
    char phone[20];
    char company[50];
    char email[50];
} Contact;

Contact contacts[100];
int contactCount = 0;
void addContact() 
{
    printf("Enter name: ");
    scanf("%s", contacts[contactCount].name);
    printf("Enter phone number: ");
    scanf("%s", contacts[contactCount].phone);
    printf("Enter company: ");
    scanf("%s", contacts[contactCount].company);
    printf("Enter email address: ");
    scanf("%s", contacts[contactCount].email);
    contactCount++;
    printf("Contact added successfully.\n");
}
void listContacts() 
{
    printf("Contacts List:\n");
    for (int i = 0; i < contactCount; i++) 
    {
        printf("Name: %s, Phone: %s, Company: %s, Email: %s\n",contacts[i].name, contacts[i].phone, contacts[i].company, contacts[i].email);
    }
}
void searchContacts() 
{
    char keyword[50];
    printf("Enter name or phone number to search: ");
    scanf("%s", keyword);
    printf("Search Results:\n");
    for (int i = 0; i < contactCount; i++) 
    {
        if (strstr(contacts[i].name, keyword) != NULL || strstr(contacts[i].phone, keyword) != NULL)
        {
            printf("Name: %s, Phone: %s, Company: %s, Email: %s\n",contacts[i].name, contacts[i].phone, contacts[i].company, contacts[i].email);
        }
    }
}
void editContact()
{
    char keyword[50];
    printf("Enter name or phone number of contact to edit: ");
    scanf("%s", keyword);
    for (int i = 0; i < contactCount; i++) {
        if (strcmp(contacts[i].name, keyword) == 0 || strcmp(contacts[i].phone, keyword) == 0) 
        {
            printf("Enter new name: ");
            scanf("%s", contacts[i].name);
            printf("Enter new phone number: ");
            scanf("%s", contacts[i].phone);
            printf("Enter new company: ");
            scanf("%s", contacts[i].company);
            printf("Enter new email address: ");
            scanf("%s", contacts[i].email);
            printf("Contact edited successfully.\n");
            return;
        }
    }
    printf("Contact not found.\n");
}

void deleteContact() 
{
    char keyword[50];
    printf("Enter name or phone number of contact to delete: ");
    scanf("%s", keyword);
    for (int i = 0; i < contactCount; i++) 
    {
        if (strcmp(contacts[i].name, keyword) == 0 || strcmp(contacts[i].phone, keyword) == 0) 
        {
            for (int j = i; j < contactCount - 1; j++) 
            {
                strcpy(contacts[j].name, contacts[j + 1].name);
                strcpy(contacts[j].phone, contacts[j + 1].phone);
                strcpy(contacts[j].company, contacts[j + 1].company);
                strcpy(contacts[j].email, contacts[j + 1].email);
            }
            contactCount--;
            printf("Contact deleted successfully.\n");
            return;
        }
    }
    printf("Contact not found.\n");
}
int main() {
    int choice;
    do {
        printf("\n--- Contact List Menu ---\n");
        printf("1. Add new contact\n");
        printf("2. List all contacts\n");
        printf("3. Search contacts\n");
        printf("4. Edit contact\n");
        printf("5. Delete contact\n");
        printf("6. Exit\n");
        printf("Enter your choice: ");
        scanf("%d", &choice);
        switch (choice) 
        {
            case 1:
                addContact();
                break;
            case 2:
                listContacts();
                break;
            case 3:
                searchContacts();
                break;
            case 4:
                editContact();
                break;
            case 5:
                deleteContact();
                break;
            case 6:
                printf("Exiting program.\n");
                break;
            default:
                printf("Invalid choice. Please try again.\n");
        }
    } while (choice != 6);
    return 0;
}
