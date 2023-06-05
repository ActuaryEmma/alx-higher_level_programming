#include <stdio.h>
#include "lists.h"
#include <stdlib.h>
/**
  * check_cycle - checks if there is a cycle in a linked list
  * @list: pointer of a linked list
  * Return: 0 if there is no cycle, 1 if there is a cycle
  */
int check_cycle(listint_t *list)
{
	/* used to traverse ,check for a cycle and assigns the first value */
	listint_t *list2 = list;

	/*list->next != NULL - helps in accessing only valid memory address*/
	while (list != NULL && list->next != NULL)
	{
		list2 = list2->next;
		list = list->next->next;

		/*checks when list and list2 are equal / when we have a cycle*/
		if (list == list2)
		{
			return (1);
		}
	}
	return (0);
}
