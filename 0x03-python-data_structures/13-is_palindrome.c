#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is palindrome or not
 * @head: address of head of the singly linked list
 * Return: 1 if palindrome and 0 if not
 */
int is_palindrome(listint_t **head)
{
	size_t len, i;
	listint_t *node1, *node2;

	if (!head)
		return (1);
	len = listint_len(*head);
	if (!len)
		return (1);
	for (i = 0; i < (len / 2); i++)
	{
		node1 = get_nodeint_at_index(*head, i);
		node2 = get_nodeint_at_index(*head, (len - 1 - i));
		if (node1->n != node2->n)
			return (0);
	}
	return (1);
}

/**
 *listint_len - counts the number of nodes in a singly linked list
 *@h: the head of the list
 *Return: the number of nodes
 */
size_t listint_len(listint_t *h)
{
	listint_t *tmp;
	size_t count = 0;

	tmp = h;
	if (h == NULL)
		return (0);
	while (tmp)
	{
		count++;
		tmp = tmp->next;
	}
	return (count);
}

/**
 *get_nodeint_at_index - returns the nth node of a list
 *@head: pointer to first node
 *@index: the index of the returned node
 *Return: pointer to the nth node
 */
listint_t *get_nodeint_at_index(listint_t *head, unsigned int index)
{
	unsigned int i = 0;
	listint_t *nth;

	if (head == NULL)
		return (0);

	nth = head;
	while (i < index)
	{
		nth = nth->next;
		i++;

		if (!nth)
			return (0);

	}

	return (nth);
}
