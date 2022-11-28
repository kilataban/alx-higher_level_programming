#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - checks for cycles within a singly linked list
 * @list: A singly-linked list.
 *
 * Return: (0) for no cycle, (-1) when cycle present
 */

int check_cycle(listint_t *list)
{
	listint_t *sl, *opti;

	if (list == NULL || list->next == NULL)
		return (0);

	sl = list->next;
	opti = list->next->next;

	while (sl && opti && opti->next)
	{
		if (sl  == opti)
			return (1);

		sl = sl ->next;
		opti = opti->next->next;
	}

	return (0);
}
