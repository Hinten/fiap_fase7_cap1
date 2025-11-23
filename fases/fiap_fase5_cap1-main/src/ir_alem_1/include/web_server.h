#ifndef WEB_SERVER_H
#define WEB_SERVER_H

#include <WebServer.h>

// Function declarations
void setupWebServer();
void handleRoot();
void handleData();
void handleHealth();

#endif // WEB_SERVER_H