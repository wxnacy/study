package com.wxnacy.spring;

import java.util.List;
import java.util.Map;

import org.springframework.beans.factory.annotation.Autowired;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class UserController {

    @Autowired
    private UserRepository userRepository;

	@GetMapping("/user")
    public List<User> users(
        @RequestParam(required=false, defaultValue="wxnacy") String name
            ) {
        List<User> res = userRepository.findByName(name);
        return res;
	}

	@GetMapping("/user/{id}")
    public User user(
        @PathVariable Integer id
            ) {
        User user = userRepository.findById(id);
        return user;
	}

	@PostMapping("/user")
    public User create(
        @RequestBody Map<String, String> body
            ) {
        User user = new User(body.get("name"));
        User item = userRepository.save(user);
        return item;
	}
}
