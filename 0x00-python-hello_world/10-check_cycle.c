#include "lists.h"

/**
 * check_cycle - checks if singly linked list has a cycle inside it
 * @list: the head node passed to us
 * Return: 0 cycle, 1 if cycle.
 */

int check_cycle(listint_t *list)
{
	listint_t *fast = NULL;
	listint_t *slow = NULL;

	if (!list || !list->next)
		return (0);

	slow = list;
	fast = list->next;

	while (fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;

		if (slow == fast)
			return (1);
	}
	return (0);
}
