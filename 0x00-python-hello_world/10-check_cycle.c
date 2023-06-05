#include <stdio.h>
#include "lists.h"
#include <stdlib.h>
int check_cycle(listint_t *list)
{
	/* used to traverse and check for a cycle */
	listint_t *list2 = list;

	while (list != NULL && list->next != NULL)
	{
		list2 = list2->next;
		list = list->next->next;
		if (list == list2)
		{
			return (1);
		}
	}
	return (0);
}
