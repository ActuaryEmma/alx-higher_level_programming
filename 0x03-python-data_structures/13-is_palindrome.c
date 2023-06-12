#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
  * is_palindrome - list that is the same from left to right and vice versa
  * split the linked list in the middle
  * @head: pointer to the head
  * Return: 0 if not palindrome, 1 if palindrome
  */
void reverse_list(listint_t **head);
int compareLists(listint_t *list1, listint_t *list2);
int is_palindrome(listint_t **head)
{
		   listint_t *slow = *head;
    listint_t *fast = *head;
    listint_t *prev = NULL;
    listint_t *temp = NULL;
    int result = 1;

    if (*head == NULL || (*head)->next == NULL)
        return (result);

    while (fast != NULL && fast->next != NULL)
    {
        fast = fast->next->next;
        prev = slow;
        slow = slow->next;
    }

    if (fast != NULL)
    {
        slow = slow->next;
    }

    temp = slow;
    reverse_list(&temp);
    *head = temp;

    while (temp != NULL)
    {
        if ((*head)->n != temp->n)
        {
            result = 0;
            break;
        }
        *head = (*head)->next;
        temp = temp->next;
    }

    reverse_list(head);

    if (prev != NULL)
        prev->next = slow;
    else
        *head = slow;

    return (result);
}

void reverse_list(listint_t **head)
{
		listint_t *current = *head, *next = NULL, *prev = NULL;

		while (current != NULL)
		{
				next = current->next;
				current->next = prev;
				prev = current;
				current = next;
		}
		*head = prev;
}
int compareLists(listint_t *list1, listint_t *list2)
{
		while (list1 != NULL && list2 != NULL)
		{
				if (list1->n != list2->n)
				{
						return (0);
				}
				list1 = list1->next;
				list2 = list2->next;
		}
		if (list1 == NULL && list2 == NULL)
		{
				return (1);
		}
		return (0);
}
