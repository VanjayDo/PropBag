package com.upc.test.dao;

import com.upc.test.entity.User;
import org.springframework.data.repository.CrudRepository;

public interface UserDAO extends CrudRepository<User, Integer> {
    User findFirstByUsername(String username);
}
