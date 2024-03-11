#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

/**
 * create_zombie_processes - to create zombie processes
 * @num_processes: the number to create
*/
void create_zombie_processes(int num_processes)
{
	pid_t pid;

	for (int i = 0; i < num_processes; i++)
	{
		pid = fork();
		if (pid < 0)
		{
			perror("fork");
			exit(EXIT_FAILURE);
		} else if (pid == 0)
		{
			printf("Zombie process created, PID: %d\n", getpid());
			exit(EXIT_SUCCESS);
		}
	}
}

/**
 * main - the main thing
 * Return: 0 on success, otherwise otherwise
*/
int main(void)
{
	int num_processes = 5;

	create_zombie_processes(num_processes);

	while (1)
	{
		sleep(1);
	}

	return (0);
}
