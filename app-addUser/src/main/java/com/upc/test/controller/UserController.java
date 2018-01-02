package com.upc.test.controller;

import com.upc.test.dao.UserDAO;
import com.upc.test.entity.User;
import com.upc.test.service.UserService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("UserController")
public class UserController {
    @Autowired
    private UserService userService;
    @Autowired
    private UserDAO userDAO;

    @RequestMapping(value = "/add", method = RequestMethod.POST)
    public String add(String username, String pwd) {
        System.out.println("username is: " + username);
        System.out.println("pwd is: " + pwd);

        if (userDAO.findFirstByUsername(username) == null) {
            userService.AddUser(username, pwd);
            return "success";
        } else {
            return "false";
        }
    }

    @RequestMapping(value = "/list", method = RequestMethod.GET)
    public Object list() {
        return userService.ListUser();
    }

    @RequestMapping(value = "/test")
    public String test() {
        System.out.println("this is just a test");
        return "test success";
    }
}