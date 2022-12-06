#include <stddef.h>
#include "lists.h"

/**
 * is_palindrome - determines if the word is a palindrome
 * @head: pointer to the head node
 * Return: On Success (1), else (0)
 */
int is_palindrome(listint_t **head)
{
	unsigned int len = 1;
	listint_t *temp;

	if (head == NULL || *head == NULL)
		return (0);

	temp = *head;
	while (temp)
	{
		temp = temp->next;
		len++;
	}
	return (1);
}
