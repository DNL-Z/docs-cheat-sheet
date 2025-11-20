# 🌐 Web Development

A comprehensive reference guide for web development fundamentals, covering essential concepts, acronyms, protocols, APIs, HTTP methods, and networking basics.

## 📑 Table of Contents

- [👥 Roles & Concepts](#-roles--concepts)
  - [CTO - Chief Technical Officer](#cto---chief-technical-officer)
  - [OOP - Object-Oriented Programming](#oop---object-oriented-programming)
  - [Paradigm](#paradigm)
  - [Design Patterns](#design-patterns)
- [🌐 Networking Basics](#-networking-basics)
  - [IP Address](#ip-address)
  - [NAT - Network Address Translation](#nat---network-address-translation)
  - [LAN - Local Area Network](#lan---local-area-network)
  - [Socket](#socket)
- [🏗️ Web Architecture](#-web-architecture)
  - [DOM - Document Object Model](#dom---document-object-model)
  - [HTTP - Hypertext Transfer Protocol](#http---hypertext-transfer-protocol)
  - [CORS - Cross-Origin Resource Sharing](#cors---cross-origin-resource-sharing)
  - [CDN - Content Delivery Network](#cdn---content-delivery-network)
- [🔌 APIs](#-apis)
  - [What is an API?](#what-is-an-api)
  - [SOAP vs REST](#soap-vs-rest)
  - [AJAX - Asynchronous JavaScript and XML](#ajax---asynchronous-javascript-and-xml)
  - [JSON - JavaScript Object Notation](#json---javascript-object-notation)
- [📦 Package Managers](#-package-managers)
  - [Homebrew](#homebrew)
  - [NPM & Yarn](#npm--yarn)
  - [Composer](#composer)
- [🔍 Development Tools](#-development-tools)
  - [Linting](#linting)
  - [XML - Extensible Markup Language](#xml---extensible-markup-language)
- [🌐 HTTP Methods](#-http-methods)
  - [OPTIONS](#options)
  - [GET](#get)
  - [POST](#post)
  - [PUT](#put)
  - [DELETE](#delete)
- [📊 HTTP Status Codes](#-http-status-codes)
  - [Success Codes (2xx)](#success-codes-2xx)
  - [Redirection Codes (3xx)](#redirection-codes-3xx)
  - [Client Error Codes (4xx)](#client-error-codes-4xx)
  - [Server Error Codes (5xx)](#server-error-codes-5xx)
- [🔄 Request States](#-request-states)
  - [XMLHttpRequest Ready States](#xmlhttprequest-ready-states)
  - [Response Properties](#response-properties)

---

## 👥 Roles & Concepts

### CTO - Chief Technical Officer

The CTO is responsible for orienting the technological strategy within an organization to help achieve its goals. They oversee innovation, technical deployment, and technological development aligned with business growth. This role embodies the essence of developer curiosity, requiring constant awareness of emerging technological trends.

### OOP - Object-Oriented Programming

Object-Oriented Programming is a programming methodology that consists of defining objects with specific characteristics, which are then inherited by child objects.

### Paradigm

A way of approaching problems according to specific rules and determining which programming language to use.

### Design Patterns

A methodology for thinking about and organizing code structure.

---

## 🌐 Networking Basics

### IP Address

**Internet Protocol Address** - A unique number assigned temporarily or permanently to a computer connected to a network that uses the Internet Protocol.

### NAT - Network Address Translation

In computer networking, NAT is when a router maps IP addresses to other IP addresses. A common use case is allowing machines with private addresses (part of an intranet, neither unique nor routable on the Internet) to communicate with the rest of the Internet using external public addresses that are unique and routable.

### LAN - Local Area Network

A local network that designates devices connected via Wi-Fi or wired connection in your home or office.

### Socket

A connection endpoint.

---

## 🏗️ Web Architecture

### DOM - Document Object Model

The **Document Object Model** is a programming interface for HTML, XML, and SVG documents. It provides a structured representation of the document as a tree and defines how the structure can be manipulated by programs in terms of style and content. The DOM represents the document as a set of nodes and objects with properties and methods. Nodes can have event handlers that trigger when an event occurs, allowing web page manipulation through scripts and programming languages.

### HTTP - Hypertext Transfer Protocol

HTTP is the protocol for exchanging information on the web. Its secure equivalent is HTTPS.

**Protocol structure:**
- **Client** ⇔ **Server**
- **Mechanism:** Request / Response

### CORS - Cross-Origin Resource Sharing

CORS is a mechanism that adds HTTP headers to allow a user agent to access resources from a server located on a different origin than the current site. A user agent makes a cross-origin HTTP request when requesting a resource from a different domain, protocol, or port than those used for the current page.

### CDN - Content Delivery Network

A CDN allows importing a library directly into HTML code.

---

## 🔌 APIs

### What is an API?

**Application Programming Interface** - An interface that allows different software applications to communicate with each other.

### SOAP vs REST

**Types:**

**SOAP** - Simple Object Access Protocol
- Relies exclusively on XML to send messages

**REST** - Representational State Transfer
- Often relies on a simple URL and can use four different HTTP 1.1 request methods (GET, POST, PUT, DELETE) to perform tasks

### AJAX - Asynchronous JavaScript and XML

AJAX is equivalent to an asynchronous HTTP request to a web server to retrieve or send data in various formats.

**Synchronous Exchange:**
- The requester waits for the requested information to be provided
- Example: Phone conversation, taking turns

**Asynchronous Exchange:**
- The requester can do other things while waiting for the response
- Example: Responding to an email and doing other tasks while waiting for a reply

**Important Notes:**
- AJAX requests are limited by their "same origin policy" (Cross Domain restriction)
- This means you cannot query two different domains (for security)
- It's possible to enable **Cross Origin Resource Sharing** on a web server to authorize requests from other domains

### JSON - JavaScript Object Notation

JSON is a lightweight data format that uses key-value pairs:

```json
{
  "key": "value"
}
```

---

## 📦 Package Managers

### Homebrew

The package manager for macOS, free and open-source written in Ruby. Its purpose is to simplify program installation. The software gained popularity within the Ruby on Rails community and received praise for its scalability.

```bash
  brew --version
```

### NPM & Yarn

**NPM** is the official package manager for Node.js. Since Node.js version 0.6.3, npm is part of the environment and is automatically installed by default. NPM works with a terminal and manages dependencies for an application.

```bash
  npm -v
```

### Composer

**Composer** is a free dependency management software written in PHP. It allows users to declare and install libraries that the main project needs. Development began in April 2011 with the first version released on March 1, 2012.

```bash
  composer --version
```

```bash
  composer self-update
```

---

## 🔍 Development Tools

### Linting

Linting is the process of running a program that analyzes code for potential errors.

### XML - Extensible Markup Language

XML is a file format designed to transmit information. It's not limited to exchanges between humans or between an application and a human; XML is equally, if not better, designed for exchanges between computer applications.

---

## 🌐 HTTP Methods

### OPTIONS

In CORS, a preflight request is sent with the OPTIONS method so the server indicates whether the request is acceptable with the specified parameters.

### GET

Allows **retrieving resources**, such as the current weather from a weather service.

### POST

Allows **creating or modifying a resource**, such as creating a new user in your application.

### PUT

Allows **modifying a resource**, such as the name of the user you just created with POST.

### DELETE

Allows **deleting a resource**, such as a comment in a discussion thread.

---

## 📊 HTTP Status Codes

### Success Codes (2xx)

**200** - Indicates everything went well

**201** - Indicates everything went well and a new resource was successfully created

**204** - Indicates everything went well, but no result is returned

### Redirection Codes (3xx)

**301** & **302** - Redirection

### Client Error Codes (4xx)

**400** - Indicates a malformed request

**401** - Indicates the user is not authenticated when it's required

**403** - Indicates the user doesn't have permission to access this resource (access denied)

**404** - Indicates the requested resource doesn't exist (page not found)

### Server Error Codes (5xx)

**500** - Indicates the server suffered an internal error (server error)

**502** - Indicates the server, acting as a gateway or proxy, received an invalid response from the upstream server

**504** - The server is not responding

**522** - Interface problem

---

## 🔄 Request States

### XMLHttpRequest Ready States

**UNSENT** (code 0) - The object is ready but the `open()` method hasn't been called yet

**OPENED** (code 1) - `open()` has been called

**HEADERS_RECEIVED** (code 2) - `send()` has been called, headers and status are available within the object

**LOADING** (code 3) - Receiving in progress, received data is partial

**DONE** (code 4) - Request completed

### Response Properties

**ReadyState** - Contains the request state

**Status** - Contains the request status code
- 2xx when everything went well
- 3xx for redirections
- 4xx for errors

**ResponseText** - Contains the web service response in text format. If the expected text is in JSON format, it must be transformed into a JavaScript object with the `JSON.parse(textJSON)` function, or conversely `JSON.stringify(jsonBody)` to convert an object to JSON.

---
