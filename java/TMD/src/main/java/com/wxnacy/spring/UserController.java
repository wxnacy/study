package com.wxnacy.spring;

import java.util.ArrayList;
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
        System.out.println(user.getId());
        User item = userRepository.save(user);
        System.out.println(item.getId());
        item = userRepository.save(user);
        System.out.println(item.getId());
        item = userRepository.saveAndFlush(user);
        System.out.println(item.getId());

        List<User> users = new ArrayList();
        users.add(new User("haah"));
        users.add(new User("ssss"));
        // List<User> items = userRepository::save(users);
        // for(int i = 0; i < items.size(); i++){
            // System.out.println(items.get(i).getId());

        // }

        new Thread(new Runnable() {
            @Override
            public void run() {
            System.out.println("Before Java8, too much code for too little to do");
            }
        }).start();

        new Thread( () -> System.out.println("In Java8, Lambda expression rocks !!") ).start();


        return item;
	}
}
