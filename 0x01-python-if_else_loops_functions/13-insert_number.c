#include "lists.h"

listint_t *insert_node(listint_t **head, int number)
{
		unsigned int i;
		listint_t *newnode, *temp;

		if (*head == NULL)
		{
				return (NULL);
		}
		newnode = (listint_t *)malloc(sizeof(listint_t));
		if (newnode == NULL)
		{
				return (NULL);
		}
		newnode->n = n;
		if (idx == 0)
		{
				newnode->next = *head;
				*head = newnode;
				return (newnode);
		}
		temp = *head;
		for (i = 0; i < idx - 1 && temp != NULL; i++)
		{
				temp = temp->next;
		}
		newnode->next = temp->next;
		temp->next = newnode;
		return (*head);
}
