#include "lists.h"

/**
 * insert_node - inserts a number in a singly-linked list
 * @head: head of the list
 * @number: number to insert
 *
 * Return: the address of the new node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *current = *head;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	new->next = NULL;
	if (current == NULL || current->n >= number)
	{
		new->next = current;
		*head = new;
		return (current);
	}
	while (current && current->next && current->next->n < number)
		current = current->next;
	new->next = current->next;
	current->next = new;
	return (new);
}
