import 'package:cloud_firestore/cloud_firestore.dart';
import 'package:flutter/material.dart';

class LogList extends StatefulWidget {
  const LogList({super.key});

  @override
  State<LogList> createState() => _LogListState();
}

class _LogListState extends State<LogList> {
  final Stream<QuerySnapshot> _usersStream =
      FirebaseFirestore.instance.collection('log').snapshots();
  @override
 Widget build(BuildContext context) {
    return StreamBuilder<QuerySnapshot>(
      stream: _usersStream,
      builder: (BuildContext context, AsyncSnapshot<QuerySnapshot> snapshot) {
        if (snapshot.hasError) {
          return const Text('Something went wrong');
        }

        if (snapshot.connectionState == ConnectionState.waiting) {
          return const Text("Loading");
        }

        return ListView(
          children: snapshot.data!.docs
              .map((DocumentSnapshot document) {
               
                return Padding(
                  padding: const EdgeInsets.all(4.0),
                  child: Card(
                    child: Padding(
                      padding: const EdgeInsets.all(16.0),
                      child: ExpansionTile(title: Text(document.id),children: [Text(document.data().toString())],),
                    ),
                   
                  ),
                );
              })
              .toList()
              .cast(),
        );
      },
    );
  }
}