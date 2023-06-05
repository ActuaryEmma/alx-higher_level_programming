#include <stdio.h>
#include "lists.h"
#include <stdlib.h>
int check_cycle(listint_t *list)
{
	/* used to traverse and check for a cycle */
	listint_t *list2 = NULL;

	while (list != NULL)
	{
		/* This part assigns the first value of list2 */
		if (list2 == NULL)
		{
			list2 = list;
		}
		else
		{
			list2 = list2->next;
		}
		list = list->next->next;
		if (list == list2)
		{
			return (1);
		}
	}
	return (0);
}
