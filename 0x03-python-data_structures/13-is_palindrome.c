#include <stdio.h>
#include "lists.h"

int is_palindrome(listint_t **head)
{
	listint_t *first;
	listint_t *last;

	int i, j, len, count = 0, tope = 0;

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
			break;
		count++;
		first = first->next;
	}
	if (count == len / 2)
		return (1);
	return (0);
}
