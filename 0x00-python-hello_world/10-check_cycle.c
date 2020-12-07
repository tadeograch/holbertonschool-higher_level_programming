#include "lists.h"
/**
 * check_cycle - checks for a cycle in a linked list.
 * @list: pointer to list to be checked.
 * Return: 0 if there is no cycle, 1 if there is a cycle.
 */                                                                                                                                                       int check_cycle(listint_t *list)
 {
	 listint_t *tmp;

	 if (list == NULL)
		 return (0);
	 while(list)
	 {
		 tmp = list;
		 list = list->next;
		 if (tmp <= list)
			 return (1);
	 }
	 return (0);
 }
