#include <stdio.h>
#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to the head of the list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *first;
	listint_t *last;
	int i, j, len, tope = 0;

	if (!head)
		return (0);
	for (len = 0, first = *head; first != NULL; len++)
	{
		first = first->next;
	}
	tope = len;
	for (i = 0, first = *head; i < len / 2; i++)
	{
		last = *head;
		for (j = 1; j < tope; j++)
		{
			last = last->next;
		}

		tope--;
		if (first->n != last->n)
			return (0);
		first = first->next;
	}
	return (1);
}
