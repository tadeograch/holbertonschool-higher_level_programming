#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
* insert_node - inserts a number into a sorted singly linked list.
* @head: head of the list
* @number: number to add
* Return:  the address of the new node, or NULL if it failed
*/
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node;
	listint_t *new_node;

	if (!head)
		return (NULL);
	node = *head;
	new_node = malloc(sizeof(listint_t));
	if (!new_node)
	{
		free(new_node);
		return (NULL);
	}
	if (number <= node->n)
	{
		new_node->n = number;
		new_node->next = node;
		node = new_node->next;
		*head = new_node;
		return (new_node);
	}
	while (node)
	{
		if (node->next == NULL)
		{
			return (add_nodeint_end(head, number));
		}
		if ((number > node->n) && (number <= (node->next)->n))
		{
			new_node->n = number;
			new_node->next = node->next;
			node->next = new_node;
			return (new_node);
		}
		node = node->next;
	}
	free(new_node);
	return (NULL);
}