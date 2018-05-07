package com.upc.test.service;

import com.upc.test.dao.UserDAO;
import com.upc.test.entity.User;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;


@Service
public class UserService {

    @Autowired
    private UserDAO userDAO;

    public void AddUser(String username, String pwd) {
        User user = new User();
        user.setUsername(username);
        user.setPwd(pwd);
        userDAO.save(user);
    }

    public Object ListUser() {
        return userDAO.findAll();
    }

}
