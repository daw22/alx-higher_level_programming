#include "lists.h"

/**
 * reverse_list - reverses a linked-list
 * @head: pointer to the head node
 * Return: pointer to the new head
 */
void reverse_list(listint_t **head)
{
	listint_t *before = NULL;
	listint_t *current = *head;
	listint_t *next = NULL;

	while (current)
	{
		next = current->next;
		current->next = before;
		before = current;
		current = next;
	}

	*head = before;
}

/**
 * is_palindrome - checks if a linked list is a palindrome
 * @head: double pointer to the linked list
 *
 * Return: 1 if it is, 0 if not
 */
int is_palindrome(listint_t **head)
{
	listint_t *start = *head, *end = *head, *temp = *head, *dup = NULL;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	while (1)
	{
		end = end->next->next;
		if (end != NULL)
		{
			dup = start->next;
			break;
		}
		if (end->next != NULL)
		{
			dup = start->next->next;
			break;
		}
		start = start->next;
	}

	reverse_list(&dup);

	while (dup && temp)
	{
		if (temp->n == dup->n)
		{
			dup = dup->next;
			temp = temp->next;
		}
		else
			return (0);
	}

	if (!dup)
		return (1);

	return (0);
}
