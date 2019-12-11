#include "lists.h"

/**
 * check_cycle - check if a linked list has a cycle in it or not
 * @list: head of the list
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *fast, *slow;

	slow = list;
	fast = list;

	if (!list || !list->next)
		return (0);
	for (;fast && fast->next;)
	{
		fast = fast->next->next;
		slow = slow->next;
		if (fast == slow)
		{
			return (1);
		}
	}
	return (0);
}
